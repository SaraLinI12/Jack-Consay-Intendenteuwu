package ejercicios3;

public class ejercicios3.7 {
    static Scanner lt= new Scanner(System.in);
   public static void main(String[] args) {
       //Declarar variables
       int edad;
       double promedio; 
       String resBeca;
       //Datos de entrada 
       System.out.println("ingrese la edad:");
       edad=lt.nextInt();
       System.out.println("Ingrese promedio:");
       promedio=lt.nextDouble();
       //proceso
       if (edad>18) {
          if (promedio>=18) {
              resBeca="Le corresponde el monto de 2000";   
          } else if (promedio>=15) {
              resBeca="Le corresponde el monto de 1000";     
          } else if (promedio<15 && promedio>=12) {
              resBeca="Le corresponde el monto de 500";
          } else  {
              resBeca="Enviar una carta para que estudie";   
          } else   {
}
