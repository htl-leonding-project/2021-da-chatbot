import {Component, OnInit} from '@angular/core';
import {BotService, IMessage} from '../../shared/bot.service';

@Component({
  selector: 'app-messages',
  templateUrl: './messages.component.html',
  styleUrls: ['./messages.component.css']
})
export class MessagesComponent implements OnInit {

  public messages: IMessage[];

  constructor(private readonly botService: BotService) {
    this.messages = [];
  }

  public ngOnInit(): void {
    this.botService.messageStream
      .subscribe((newMsg: IMessage) => {
        this.messages.push(newMsg);
      });
  }

}
