import { Injectable } from "@angular/core";
import { Subject } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class LoaderService{

    constructor(){}
    
    loadingSubject= new Subject<any>();

    start(){
        setTimeout(()=> this.loadingSubject.next(true), 1);
    }
    stop(){
        setTimeout(()=> this.loadingSubject.next(false), 1);
    }
}