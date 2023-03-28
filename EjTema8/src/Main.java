public class Main {
    public static void main(String[] args) {
        Persona person = new Persona();

        person.setEdad(22);
        person.setNombre("Victor");
        person.setTelefono("5569125874");

        System.out.println("Nombre: "+person.getNombre()+"\nEdad: "+person.getEdad()+"\nTelefono: "+person.getTelefono());
    }

    }
class Persona{
    private int edad;
    private String nombre;
    private String telefono;

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }
}