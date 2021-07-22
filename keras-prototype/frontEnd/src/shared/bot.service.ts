import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable, Subject} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BotService {
  private readonly messageProvider: Subject<IMessage>;
  private chatId: number | null;

  constructor(private readonly http: HttpClient) {
    this.messageProvider = new Subject();
    this.chatId = null;
  }

  public async postMessage(message: IMessage): Promise<void> {
    const result = await this.http.get<IServerMessage>('http://localhost:5000/api/ChatBot?question=' + message.message, {
    }).toPromise();
    if (result.name !== ''){
      message.user = result.name;
    }else {
      message.user = 'User';
    }
    this.addMessage(message);
    this.addMessage({
      user: 'ChatBot',
      message: result.message,
    });
  }

  public get messageStream(): Observable<IMessage> {
    return this.messageProvider;
  }

  private addMessage(message: IMessage): void {
    this.messageProvider.next(message);
  }

}

export interface IMessage {
  user: string;
  readonly message: string;
}
interface IServerMessage {
  readonly name: string;
  readonly message: string;
}
