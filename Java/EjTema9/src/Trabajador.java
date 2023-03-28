public class Trabajador extends Persona{
    private int salario;

    public Trabajador(int edad, String nombre, String telefono, int salario) {
        super(edad, nombre, telefono);
        this.salario = salario;
        System.out.println("Soy un Trabajador\n");
    }

    public int getSalario() {
        return salario;
    }

    public void setSalario(int salario) {
        this.salario = salario;
    }
}
