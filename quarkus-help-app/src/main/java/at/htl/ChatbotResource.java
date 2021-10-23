package at.htl;

import at.htl.entity.*;
import at.htl.repository.C_EntityRepository;
import at.htl.repository.C_ResponseRepository;
import at.htl.repository.IntentRepository;
import org.postgresql.shaded.com.ongres.scram.common.bouncycastle.pbkdf2.Strings;

import javax.persistence.Transient;
import javax.transaction.Transactional;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

@Path("/api")
public class ChatbotResource {

    C_EntityRepository cEntityRepository = new C_EntityRepository();
    C_ResponseRepository cResponseRepository = new C_ResponseRepository();
    IntentRepository intentRepository = new IntentRepository();
    @GET
    @Transactional
    @Produces(MediaType.APPLICATION_JSON)
    @Path("/fill")
    public C_Entity hello() {
        C_Entity e = new C_Entity();
        e.setEntType(EntType.Produkt);
        e.setName("HTL Leonding");
        List<String> values = new ArrayList<>();
        values.add("HTL Leonding");
        values.add("HTL");
        values.add("Höhere technische Lehranstalt");
        e.setValues(values);

        Intent intent = new Intent();
        e.setIntent(intent);
        intent.setEntity(e);
        List<String> sentences = new ArrayList<>();
        sentences.add("Erzähl mir etwas über die {ENT}");
        sentences.add("Was ist die {ENT}");
        sentences.add("{ENT}");
        intent.setSentences(sentences);

        C_Response response = new C_Response();
        response.setResType(ResType.Text);
        List<String> responses = new ArrayList<>();
        responses.add("Die HTL Leonding ist eine Höhere Schule in Leonding in der man zwischen 4 Zweigen wählen kann");
        responses.add("Die HTL ist eine Schule");
        response.setSentences(responses);

        intent.setResponse(response);

        cResponseRepository.persist(response);
        intentRepository.persist(intent);
        cEntityRepository.persist(e);
        return e;
    }

    @GET
    @Transactional
    @Path("/create")
    @Produces(MediaType.APPLICATION_JSON)
    public String create() {
        String output = "version: \"2.0\"\n" +
                "nlu:\n";
        try {
            File myObj = new File("nlu.yml");
            if (myObj.createNewFile()) {
                System.out.println("File created: " + myObj.getName());
            } else {
                System.out.println("File already exists.");
            }
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        try {
            FileWriter myWriter = new FileWriter("nlu.yml");
            List<Intent> intents = intentRepository.listAll();
            System.out.println(intents);
            for (Intent intent: intents) {
                output += "- intent: "+intent.getEntity().getName()+"\n";
                output += "  examples: |\n";
                for(String entity: intent.getEntity().getValues()){
                    for (String intentSentence: intent.getSentences()){
                        output += "    - "+intentSentence.replace("{ENT}","["+entity+"]("+intent.getEntity().getName()+")\n");
                    }
                }
            }
            myWriter.write(output);
            myWriter.close();
            System.out.println("Successfully wrote to the file.");
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        return output;
    }
}
