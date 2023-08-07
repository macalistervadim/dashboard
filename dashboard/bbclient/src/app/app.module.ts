import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { BbListComponent } from './bb-list.component';
import { BbDetailComponent } from './bb-detail.component';
import { BbService } from "./bb.service";
import { FormsModule } from "@angular/forms";
import {HttpClientModule} from "@angular/common/http";
import { registerLocaleData } from "@angular/common";
import locateRu from '@angular/common/locales/ru'
import locateRuExtra from '@angular/common/locales/extra/ru'
import { LOCALE_ID } from "@angular/core";
import { Routes } from "@angular/router";
import { RouterModule } from "@angular/router";

registerLocaleData(LocaleRu, 'ru', locateRuExtra)

const appRoutes: Routes = [
  {path: ':pk', component: BbDetailComponent},
  {path: '', component: BbListComponent}
]

@NgModule({
  declarations: [
    AppComponent,
    BbListComponent,
    BbDetailComponent
  ],
  imports: [
    RouterModule.forRoot(appRoutes),
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [
    BbService,
    {provide: LOCALE_ID, useValue: 'ru'}
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

