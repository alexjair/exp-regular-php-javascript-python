
//Falta solucionar los errores

import java.io.BufferedReader;
import java.io.FileReader;
import java.io:IOException;

public  class express{

    public static void main(String[] args){
        //String file = "./results.csv";
        String file = "expresion_regular/files/results.csv";

        try{
            BufferedReader br = new BufferedReader(new FileReader(file));
            String line;
            while((line = br.readLine()) != null){
                system.out.println(line);
            }
        }catch(Exception e){
            system.out.println("nope!");
        }
    }
}