
/*
DESAFIO!!!
Implemente um algoritmo para inverter a ordem de uma string em sua
linguagem de programacao favorita. Nao use funcoes/metodos prontos.
*/

public class main {
    public static void main(String[] args) {
		
		
		String palavra = "Hello World!";
		String invertida = "";
		
        for (int i = palavra.length()-1; i >= 0; i--) { 
            invertida += palavra.charAt(i);
        } 
        System.out.println("A palavra: " + palavra + " invertida ficará: " + invertida);
	}
}