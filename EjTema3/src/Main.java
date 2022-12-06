public class Main {
    public static void main(String[] args) {
        //Primera parte
        //Crear una función con tres parámetros que sean números que se suman entre sí.
        //Llamar a la función en el main y darle valores
        int resultado = suma(1,2,3);
        System.out.println("Parte 1: "+resultado);

        Coche miCoche = new Coche();
        miCoche.aumtentarPuertas();

        System.out.println("Parte 2: "+miCoche.numPuertas);
    }
    public static int suma(int a, int b, int c){
        return a+b+c;
    }
}
//Segunda parte:
//Crear una clase coche.
//Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.
//Una función que incremente el número de puertas que tiene el coche.
//Crear un objeto miCoche en el main y añadirle una puerta.
//Mostrar el número de puertas que tiene el objeto.
class Coche{
    public int numPuertas = 0;

    public void aumtentarPuertas(){
        this.numPuertas++;
    }
}