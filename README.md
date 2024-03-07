Text Adventure made with python, by HyunjunKimchi (Who did most of the work)
50 thousand lashings to CodeBlueJay who is a FREELOADER and is doing ABSOLUTELY NOTHING
```py
return "CodeBlueJay is gay"
```
CodeBlueJay should actually do work fr.
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
