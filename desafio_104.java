/*
    DESAFIO!!!
    1) Implemente um algoritmo para trocar o conteudo de duas variáveis x e y.
    2) Agora faca sem utilizar uma terceira variavel temporaria.
    OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
*/

public class main {
    public static void main(String[] args) {
		
		
		int a=15,b=10;
		
		System.out.println("Valor A: " + a + " Valor B: " + b);
		
		a = a^b;
        b = b^a;
        a = a^b;
		
         
        System.out.println("Valor A: " + a + " Valor B: " + b);
	}
}