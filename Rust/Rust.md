# Install

[The official site](https://www.rust-lang.org/tools/install)

```shell
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustc --version
```



# Module

[How to call a function in another file but the same crate?](https://users.rust-lang.org/t/how-to-call-a-function-in-another-file-but-the-same-crate/15214/3)

```rust
// src/hello.rs
pub fn hello() {
    println!("hello my world!");
}
```

```rust
// src/main.rs
mod hello;

fn main() {
    hello::hello();
}
```

