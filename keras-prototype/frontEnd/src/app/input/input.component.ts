import {Component} from '@angular/core';
import {BotService} from '../../shared/bot.service';

@Component({
  selector: 'app-input',
  templateUrl: './input.component.html',
  styleUrls: ['./input.component.css']
})
export class InputComponent {

  constructor(private readonly botService: BotService) {
    this.message = null;
    this.name = null;
    this.processing = false;
  }

  public message: string | null;
  public name: string | null;
  public processing: boolean;

  public async sendMessage(): Promise<void> {
    if (nullOrEmpty(this.message) || this.processing) {
      return;
    }
    this.processing = true;
    await this.botService.postMessage({
      user: this.name ?? '',
      message: this.message ?? '',
    });
    this.message = null;
    this.processing = false;
  }

}

function nullOrEmpty(s: string | null): boolean {
  return s === null || s.trim() === '';
}