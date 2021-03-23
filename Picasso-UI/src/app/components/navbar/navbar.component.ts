import { Component, OnInit } from '@angular/core';
import { staticJson } from 'src/app/dummy/dummy-data';
import { QueryService } from 'src/app/services/query.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

}
