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
    private C_Entity entity;

    @OneToOne
    private C_Response response;

    public List<String> getSentences() {
        return sentences;
    }

    public void setSentences(List<String> sentences) {
        this.sentences = sentences;
    }

    public C_Entity getEntity() {
        return entity;
    }

    public void setEntity(C_Entity entity) {
        this.entity = entity;
    }

    public C_Response getResponse() {
        return response;
    }

    public void setResponse(C_Response response) {
        this.response = response;
    }
}
