package at.htl.entity;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.ElementCollection;
import javax.persistence.Entity;
import java.util.List;

@Entity(name = "C_RESPONSE")
public class ChatbotResponse extends PanacheEntity {

    @ElementCollection
    private List<String> sentences;

    private ResType resType;

    public List<String> getSentences() {
        return sentences;
    }

    public void setSentences(List<String> sentences) {
        this.sentences = sentences;
    }

    public ResType getResType() {
        return resType;
    }

    public void setResType(ResType resType) {
        this.resType = resType;
    }
}
