import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { Router } from '@angular/router';
import { trigger, state, style, animate, transition } from '@angular/animations';

@Component({
  selector: 'app-landing',
  templateUrl: './landing.component.html',
  styleUrls: ['./landing.component.scss'],
  animations: [
    // trigger('EnterLeave', [
    //   state('flyIn', style({ transform: 'translateX(0)' })),
    //   transition(':enter', [
    //     style({ transform: 'translateY(1000px)' }),
    //     animate('0.5s 300ms ease-in')
    //   ])
    // ])
    trigger('fadeInOut', [
      state('void', style({
        opacity: 0
      })),
      transition('void <=> *', animate(2000)),
    ]),
  ],
})
export class LandingComponent implements OnInit {

  constructor(private titleService: Title,
    private router: Router) { }

  ngOnInit() {
    this.titleService.setTitle('Docusight - Landing Page');
   
  }

  gettingStarted() {
    this.router.navigate(['/dashboard'])
  }

}
