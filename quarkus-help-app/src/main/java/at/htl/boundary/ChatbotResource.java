package at.htl.boundary;

import at.htl.entity.*;
import at.htl.repository.ChatbotEntityRepository;
import at.htl.repository.ChatbotResponseRepository;
import at.htl.repository.IntentRepository;

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

    ChatbotEntityRepository cEntityRepository = new ChatbotEntityRepository();
    ChatbotResponseRepository cResponseRepository = new ChatbotResponseRepository();
    IntentRepository intentRepository = new IntentRepository();
    @GET
    @Transactional
    @Produces(MediaType.APPLICATION_JSON)
    @Path("/fill")
    public ChatbotEntity hello() {
        ChatbotEntity e = new ChatbotEntity();
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

        ChatbotResponse response = new ChatbotResponse();
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
