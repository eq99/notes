import logging
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

logging.basicConfig(level=logging.DEBUG)


class App(object):

    def __init__(self, uri, auth):
        self.driver = GraphDatabase.driver(uri, auth=auth)

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    def create_subject(self, name):
        with self.driver.session() as session:
            # Write transactions allow the driver to handle retries and transient errors
            results = session.write_transaction(
                self._create_subject, name)
            for result in results:
                logging.info(f'Create subject {result}')

    @staticmethod
    def _create_subject(tx, name):

        # To learn more about the Cypher syntax,
        # see https://neo4j.com/docs/cypher-manual/current/

        # The Reference Card is also a good resource for keywords,
        # see https://neo4j.com/docs/cypher-refcard/current/

        query = (
            "CREATE (subject:Subject { name: $name }) "
            "RETURN subject"
        )
        results = tx.run(query, name=name)
        try:
            return [result["subject"]["name"] for result in results]
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise

    def find_subject(self, name):
        with self.driver.session() as session:
            result = session.read_transaction(self._find_suject, name)
            for record in result:
                logging.info(f"Found Subject: {record}")

    @staticmethod
    def _find_suject(tx, name):
        query = (
            "MATCH (s:Subject) "
            "WHERE s.name = $name "
            "RETURN s.name AS name"
        )
        result = tx.run(query, name=name)
        return [record["name"] for record in result]

    def create_relation(self, name1, name2, relation):
        with self.driver.session() as session:
            # Write transactions allow the driver to handle retries and transient errors
            results = session.write_transaction(
                self._create_relation, name1, name2, relation)
            for result in results:
                logging.info(
                    f'Create relation {result[0]}-[{relation}]->{result[1]}')

    @staticmethod
    def _create_relation(tx, name1, name2, relation):

        if relation == "数学基础":
            query = (
                f"MATCH (s1:Subject) WHERE s1.name = $name1 "
                "MATCH (s2:Subject) WHERE s2.name = $name2 "
                "CREATE (s1)-[:数学基础]->(s2)"
                "return s1.name as name1, s2.name as name2"
            )

        if relation == "编程基础":
            query = (
                f"MATCH (s1:Subject) WHERE s1.name = $name1 "
                "MATCH (s2:Subject) WHERE s2.name = $name2 "
                "CREATE (s1)-[:编程基础]->(s2)"
                "return s1.name as name1, s2.name as name2"
            )

        if relation == "计算机基础":
            query = (
                f"MATCH (s1:Subject) WHERE s1.name = $name1 "
                "MATCH (s2:Subject) WHERE s2.name = $name2 "
                "CREATE (s1)-[:计算机基础]->(s2)"
                "return s1.name as name1, s2.name as name2"
            )

        results = tx.run(query, name1=name1, name2=name2, relation=relation)
        try:
            return [[result['name1'], result['name2']] for result in results]
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise


if __name__ == "__main__":
    uri = "neo4j://localhost:7687"
    auth = ("neo4j", "test")
    app = App(uri, auth=auth)
    subjects = ["计算机"]
    subjects_math = ["微积分", "离散数学", "概率论", "线性代数"]
    subjects_program = ["c++", "Java", "Python"]
    subjects_computer = ["计算机组成", "计算机网络", "编译原理", "操作系统"]

    for subject in subjects+subjects_math+subjects_program+subjects_computer:
        app.create_subject(subject)

    for subject in subjects_math:
        app.create_relation("计算机", subject, "数学基础")

    for subject in subjects_program:
        app.create_relation("计算机", subject, "编程基础")

    for subject in subjects_computer:
        app.create_relation("计算机", subject, "计算机基础")

    app.find_subject("计算机")
    app.close()
