public class Main {
    public static void main(String[] args) {
        Cliente cliente = new Cliente(29, "Javier","7895471236", 5000);
        cliente.imprimirPersona();
        System.out.println("Cedito: "+cliente.getCredito()+"\n");


        Trabajador trabajador = new Trabajador(30,"Victor", "5587963698", 100000);
        trabajador.imprimirPersona();
        System.out.println("Salario: "+trabajador.getSalario());
    }
}