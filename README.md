Text Adventure made with python, by CodeBlueJay (Who did ALL of the work)
50 thousand lashings to HyunJun who is a FREELOADER and is doing ABSOLUTELY NOTHING
```py
return "CodeBlueJay is cool"
```
HyunJun should actually do work fr.
```java
import java.util.Iterator;

class PrintableString implements Iterable<Character> {
    private String string;

    public PrintableString(String string) {
        this.string = string;
    }

    @Override
    public Iterator<Character> iterator() {
        return new Iterator<Character>() {
            private int index = 0;

            @Override
            public boolean hasNext() {
                return index < string.length();
            }

            @Override
            public Character next() {
                return string.charAt(index++);
            }
        };
    }
}

class CharacterPrinter {
    public void printCharacter(Character character) {
        System.out.print(character);
    }
}

public class HelloWorld {
    public static void main(String[] args) {
        PrintableString helloWorld = new PrintableString("Hello, World!");
        CharacterPrinter printer = new CharacterPrinter();

        for (Character character : helloWorld) {
            printer.printCharacter(character);
        }
    }
}
```
```rust
use std::collections::HashMap;

struct Character {
    value: char,
}

impl Character {
    fn new(value: char) -> Character {
        Character { value }
    }

    fn print(&self) {
        print!("{}", self.value);
    }
}

struct Word {
    characters: Vec<Character>,
}

impl Word {
    fn new(word: &str) -> Word {
        Word {
            characters: word.chars().map(|c| Character::new(c)).collect(),
        }
    }

    fn print(&self) {
        for character in &self.characters {
            character.print();
        }
    }
}

struct Sentence {
    words: HashMap<usize, Word>,
}

impl Sentence {
    fn new(sentence: &str) -> Sentence {
        Sentence {
            words: sentence
                .split_whitespace()
                .enumerate()
                .map(|(i, word)| (i, Word::new(word)))
                .collect(),
        }
    }

    fn print(&self) {
        for i in 0..self.words.len() {
            self.words.get(&i).unwrap().print();
            if i < self.words.len() - 1 {
                print!(" ");
            }
        }
    }
}

fn main() {
    let sentence = Sentence::new("Hello, World!");
    sentence.print();
    println!();
}
```
```c++
#include <iostream>
#include <ctime>
#include <cstdlib>

int main() {
    srand(time(0)); // seed random number generator
    int secret_number = rand() % 100 + 1; // generate secret number between 1 and 100
    int guess;

    std::cout << "Welcome to the guessing game!\n";
    std::cout << "I'm thinking of a number between 1 and 100.\n";

    do {
        std::cout << "Enter your guess: ";
        std::cin >> guess;

        if (guess < secret_number) {
            std::cout << "Too low! Try again.\n";
        } else if (guess > secret_number) {
            std::cout << "Too high! Try again.\n";
        }
    } while (guess != secret_number);

    std::cout << "Congratulations! You found the number!\n";

    return 0;
}
```
```py
import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 10

    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it.")

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        attempts -= 1

        if guess < secret_number:
            print(f"Too low! You need to guess higher. You have {attempts} attempts left.")
        elif guess > secret_number:
            print(f"Too high! You need to guess lower. You have {attempts} attempts left.")
        else:
            print(f"Congratulations! You found the number with {attempts} attempts remaining!")
            return

        if attempts == 0:
            print(f"You've run out of attempts. The secret number was {secret_number}. Better luck next time!")

guessing_game()
```