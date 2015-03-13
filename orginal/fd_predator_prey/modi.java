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
        
    	FileWriter fw1 = new FileWriter("./trf1_100.txt");
        FileWriter fw2 = new FileWriter("./trf2_100.txt");
        FileWriter fw3 = new FileWriter("./trf3_100.txt");
	FileWriter fw4 = new FileWriter("./rf1_100.txt");
        FileWriter fw5 = new FileWriter("./rf2_100.txt");
        FileWriter fw6 = new FileWriter("./rf3_100.txt");

	BufferedWriter bw1 = new BufferedWriter(fw1);
        BufferedWriter bw2 = new BufferedWriter(fw2);
        BufferedWriter bw3 = new BufferedWriter(fw3);
	BufferedReader br = new BufferedReader(new FileReader("./trf_100.txt"));
	BufferedWriter bw4 = new BufferedWriter(fw4);
        BufferedWriter bw5 = new BufferedWriter(fw5);
        BufferedWriter bw6 = new BufferedWriter(fw6);
	BufferedReader br1 = new BufferedReader(new FileReader("./reference100.txt"));    
        try {
        String line1 = br1.readLine();
        StringTokenizer st1;
             
        String line = br.readLine();
        StringTokenizer st;
        while (line != null) {
            st = new StringTokenizer(line, "  ");
            bw1.write(st.nextToken()+"\n");
            bw2.write(st.nextToken()+"\n");
            bw3.write(st.nextToken()+"\n");
            
            line = br.readLine();
            bw1.flush();
            bw2.flush();
            bw3.flush();
            }
while (line1 != null) {
            st1 = new StringTokenizer(line1, "  ");
            bw4.write(st1.nextToken()+"\n");
            bw5.write(st1.nextToken()+"\n");
            bw6.write(st1.nextToken()+"\n");
            
            line1 = br1.readLine();
            bw4.flush();
            bw5.flush();
            bw6.flush();
            }
         }catch(Exception e){br.close();
        bw1.close();
        bw2.close();
        bw3.close();
	bw4.close();
        bw5.close();
        bw6.close();
br1.close();
        }
        

    
    
    }
}
