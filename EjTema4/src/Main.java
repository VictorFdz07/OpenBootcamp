import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int max = 10; int min = -10;
        int range = max - min + 1;

        int numeroIF = (int) (Math.random() * range) + min;
        /*IF*/
        if (numeroIF > 0)
            System.out.println("IF "+numeroIF+ " Es positivo");
        else if (numeroIF < 0)
            System.out.println("IF "+numeroIF+ " Es negativo");
        else
            System.out.println("IF "+numeroIF+ " Es cero");
        /*WHILE*/
        int numeroWhile = 0;
        while (numeroWhile<3){
            System.out.println("WHILE "+numeroWhile);
            numeroWhile++;
        }
        /*DO WHILE*/
        do {
            System.out.println("DO WHILE "+numeroWhile);
            numeroWhile++;
        }while (numeroWhile<3);
        /*FOR*/
        int numeroFor = 0;
        for (int i = 0; i<=3; i++){
            System.out.println("FOR "+numeroFor);
            numeroFor++;
        }
        /*SWITCH*/
        String[] estaciones = {"Verano", "Invierno", "Otoño", "Primavera", "Ninguna"};
        Random generator = new Random();
        int r = generator.nextInt(estaciones.length);

        String estacion = estaciones[r];
        switch (estacion){
            case "Verano":
            case "Invierno":
            case "Otoño":
            case "Primavera":
            default:
                System.out.println("La estacion es: "+estacion);
                break;
        }
    }
}