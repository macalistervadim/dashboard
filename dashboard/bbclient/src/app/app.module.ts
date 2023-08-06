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

registerLocaleData(LocaleRu, 'ru', locateRuExtra)

@NgModule({
  declarations: [
    AppComponent,
    BbListComponent,
    BbDetailComponent
  ],
  imports: [
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

