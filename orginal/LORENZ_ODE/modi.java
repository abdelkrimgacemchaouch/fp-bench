import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.StringTokenizer;

/**
 *
 * @author djallal
 */
public class modi {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws FileNotFoundException, IOException {
        
    	FileWriter fw1 = new FileWriter("fichier1_64.txt");
        FileWriter fw2 = new FileWriter("fichier2_64.txt");
        FileWriter fw3 = new FileWriter("fichier3_64.txt");
	FileWriter fw4 = new FileWriter("fichier4_64.txt");
	BufferedWriter bw1 = new BufferedWriter(fw1);
        BufferedWriter bw2 = new BufferedWriter(fw2);
        BufferedWriter bw3 = new BufferedWriter(fw3);
	BufferedWriter bw4 = new BufferedWriter(fw4);
        BufferedReader br = new BufferedReader(new FileReader("lorenz_ode_data.txt"));
    
        try {
        
             String line = br.readLine();
        StringTokenizer st;
        
        while (line != null) {
            st = new StringTokenizer(line, "  ");
            bw1.write(st.nextToken()+"\n");
            bw2.write(st.nextToken()+"\n");
            bw3.write(st.nextToken()+"\n");
            bw4.write(st.nextToken()+"\n");
            line = br.readLine();
            bw1.flush();
            bw2.flush();
            bw3.flush();
	    bw4.flush();
            }
        }catch(Exception e){br.close();
        bw1.close();
        bw2.close();
        bw3.close();
	bw4.close();
}
        

    
    
    }
}
