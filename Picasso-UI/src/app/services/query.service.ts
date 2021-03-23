import { Injectable } from "@angular/core";
import { Subject } from 'rxjs';
import { GlobalHttpClientService } from '../shared/global-http.service';

@Injectable({
    providedIn: 'root'
})
export class QueryService{
    constructor(private http: GlobalHttpClientService){}
    
    getAnalytics(query: string){
        return this.http.makeGetRequest('/processquery', {query: query});
    }
}