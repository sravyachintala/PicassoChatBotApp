import { Component, HostListener, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { SuggestionsJson } from 'src/app/dummy/dummy-data';
import { LoaderService } from 'src/app/services/loader.service';
import { QueryService } from 'src/app/services/query.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  staticJson : any
  keys: string[]=[];
  values: string[] = [];
  queryControl : FormControl = new FormControl('');
  chatHistory: any[] = [];
  showNew: boolean = false;
  showSuggest: boolean = false;
  qureyResponse: any;
  closeFull : boolean = false;
  constructor(private loader: LoaderService, private query: QueryService) { }

  ngOnInit(): void {
    this.staticJson = SuggestionsJson;

  }

  sendQuery(query?: any){
    if(query){
      this.query.getAnalytics(query).subscribe((data: any)=>{
          this.closeFull = true;
          this.loader.stop();
          this.chatHistory.push({user: 'you', message: query});
          this.queryControl.reset();
          setTimeout(()=> this.scrollToBottom(), 10);
          if(data.Response.status=="success"){
            this.showNew = true;
            var message =[];
            this.qureyResponse = data.Response.visualization;
            this.keys = Object.keys(data.Response.nlp_tokens);
            for(let i=0; i < this.keys.length; i++){
              this.keys[i]=this.keys[i].toUpperCase();
              this.keys[i]=this.keys[i].replace('_', ' ');
            }
            this.values = Object.values(data.Response.nlp_tokens);
            for(let i = 0; i < this.keys.length; i++){
              var messagedata = {key: this.keys[i], value: this.values[i]};
              message.push(messagedata);
            }
            this.chatHistory.push({user: 'bot', message: message});
            console.log(this.values);
            setTimeout(()=> this.scrollToBottom(), 10)
            this.showSuggestions();
          }else{
            Swal.fire(
              'Error!',
              'Query Seems to be not working, please try another',
              'error'
            )
          }
      })
    }
    else{
      this.getQueryAnalytics();
    }
  }
  @HostListener('document:keydown.enter', ['$event']) onKeydownHandler(event: KeyboardEvent) {
    this.sendQuery();
  }
  scrollToBottom(){
    var element = document.getElementById("scollTobottom");
    element.scrollTop = element.scrollHeight;
  }
  showSuggestions(){
    this.showSuggest = !this.showSuggest;
  }
  getQueryAnalytics(){
    this.loader.start();
    if(this.queryControl.value !=null && this.queryControl.value != ''){
      this.query.getAnalytics(this.queryControl.value).subscribe((data: any)=>{
          this.closeFull = true;
        this.loader.stop();
        this.chatHistory.push({user: 'you', message: this.queryControl.value});
        this.queryControl.reset();
        setTimeout(()=> this.scrollToBottom(), 10);
        if(data.Response.status=="success"){
          this.showNew = true;
          var message =[];
          this.qureyResponse = data.Response.visualization;
          this.keys = Object.keys(data.Response.nlp_tokens);
          for(let i=0; i < this.keys.length; i++){
            this.keys[i]=this.keys[i].toUpperCase();
            this.keys[i]=this.keys[i].replace('_', ' ');
          }
          this.values = Object.values(data.Response.nlp_tokens);
          for(let i = 0; i < this.keys.length; i++){
            var messagedata = {key: this.keys[i], value: this.values[i]};
            message.push(messagedata);
          }
          this.chatHistory.push({user: 'bot', message: message});
          console.log(this.values);
          setTimeout(()=> this.scrollToBottom(), 10)
        }else{
          Swal.fire(
            'Error!',
            'Query Seems to be not working, please try another',
            'error'
          )
        }
      })
    }else{
      this.loader.stop();
    }
  }
}
