import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { NavbarComponent } from './components/navbar/navbar.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { LandingComponent } from './pages/landing/landing.component';

const routes: Routes = [
  {path:'', component: LandingComponent, pathMatch: 'full'},
  {
    path:'dashboard', 
    component: NavbarComponent, 
    pathMatch: 'full',
    children:
    [
      {path:'', component: DashboardComponent}
    ]
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
