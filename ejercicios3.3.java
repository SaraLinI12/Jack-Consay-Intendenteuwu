package ejercicios3;

public class ejercicios3.3 {
     public static void main(String[] args) {
         //Declarar variables 
          String regalo;
          int costo;
          double presupuesto;
          System.out.println("Ingrese el presupuesto:");
          presupuesto=lt.nextDouble();
          System.out.println("Ingrese el costo del regalo:");
          costo=lt.nextDouble();
          //Proceso
          if (presupuesto<=10) {
             regalo="le corresponde al costo de la tarjeta";
              } else if (presupuesto>=11&&presupuesto<=100) {
              regalo= "le corresponde al costo de el chocolate";
            } else if (presupuesto>=101&&presupuesto<=250) {
               regalo= "le corresponde al costo de las flores"; 
            } else if (presupuesto>=251) {
                regalo="le corresponde al costo del anillo";
            }
          //Datos de salida 
          System.out.println(regalo);
     
        
    } 
        
    
}
