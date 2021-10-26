package at.htl.entity;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.ElementCollection;
import javax.persistence.Entity;
import javax.persistence.OneToOne;
import java.util.List;

@Entity
public class Intent extends PanacheEntity {
    @ElementCollection
    private List<String> sentences;

    @OneToOne
    private ChatbotEntity entity;

    @OneToOne
    private ChatbotResponse response;

    public List<String> getSentences() {
        return sentences;
    }

    public void setSentences(List<String> sentences) {
        this.sentences = sentences;
    }

    public ChatbotEntity getEntity() {
        return entity;
    }

    public void setEntity(ChatbotEntity entity) {
        this.entity = entity;
    }

    public ChatbotResponse getResponse() {
        return response;
    }

    public void setResponse(ChatbotResponse response) {
        this.response = response;
    }
}
