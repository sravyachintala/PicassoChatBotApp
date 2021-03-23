import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { MaterialModule } from './shared/material-module';
import { DashboardItemsComponent } from './components/dashboard-items/dashboard-items.component';
import { LoaderComponent } from './components/loader/loader.component';
import { ChartsModule } from '@progress/kendo-angular-charts';
import 'hammerjs';
import { ReactiveFormsModule } from '@angular/forms';
import { LandingComponent } from './pages/landing/landing.component';
import { GlobalHttpClientService } from './shared/global-http.service';
import { HttpClientModule } from '@angular/common/http';



@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    LandingComponent,
    DashboardComponent,
    DashboardItemsComponent,
    LoaderComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    ReactiveFormsModule,
    MaterialModule,
    ChartsModule
  ],
  providers: [GlobalHttpClientService],
  bootstrap: [AppComponent]
})
export class AppModule { }
