import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-dashboard-items',
  templateUrl: './dashboard-items.component.html',
  styleUrls: ['./dashboard-items.component.css']
})
export class DashboardItemsComponent implements OnInit {

  @Input('Title') title : any;
  @Input('Type') type : any;
  @Input('Data') data : any;
  showPie: boolean = false;
  showBar : boolean = false;
  showTable: boolean = false;
  showNumeric: boolean = false;
  barLegends : any[]=[];
  barValues : any[]=[];
  columns: any;
  rows: any;
  colors=['#4287f5', '#e7ed40', '#cc3ef0', '#ed6432'];

  constructor() { }

  ngOnInit(): void {
    if(this.type=='pie_chart'){
      this.showPie = true;
    }else if(this.type =='bar_chart'){
      this.showBar = true;
      for(let i=0; i < this.data.length; i++){
        this.barLegends.push(this.data[i].legend);
        this.barValues.push(this.data[i].value);
      }
    }else if(this.type == 'table'){
      this.showTable = true;
    }else if(this.type=='numeric_value'){
      this.showNumeric = true;
    }
  }

}
