import {Component, OnInit} from '@angular/core';
import { BbService } from "./bb.service";
import { ActivatedRoute } from "@angular/router";
import { BbService } from './bb.service';

@Component({
  selector: 'app-bb-list',
  templateUrl: './bb-list.component.html',
  styleUrls: ['./bb-list.component.css']
})
export class BbListComponent implements OnInit{
  protected  bb: any;
  protected comments: any[] = [];
  protected author: String = '';
  protected password: String = '';
  protected content: String = '';
  constructor(private bbservice: BbService, private ar: ActivatedRoute) { }
  ngOnInit() {
    this.bbservice.getBbs().subscribe(
      (bbs: Object[]) => {this.bbs = bbs;}
    )
  }
}
