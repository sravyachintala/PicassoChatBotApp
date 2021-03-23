import { Component, OnInit } from '@angular/core';
import { LoaderService } from 'src/app/services/loader.service';

@Component({
  selector: 'app-loader',
  templateUrl: './loader.component.html',
  styleUrls: ['./loader.component.css']
})
export class LoaderComponent implements OnInit {
  show: boolean = false;
  
  constructor(private loader : LoaderService) { }

  ngOnInit(): void {
    this.loaderControl();
  }
  loaderControl(){
    this.loader.loadingSubject.subscribe((status: boolean)=>{
      this.show = status;
    })
  }
}
