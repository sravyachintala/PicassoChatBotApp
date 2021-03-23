import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from "@angular/core";
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable()
export class GlobalHttpClientService{
    private apiUrl = environment.ApiUrl;
    constructor(private client: HttpClient){}
    /**
     * Make a GET Request
     * @params url
     * @params params
     * @returns { Observable<any> }
     */
    makeGetRequest(url: string, params?: any) : Observable<any>{
        return this.client.get(this.apiUrl+url, {params: params})
    }
    /**
     * Make a POST request
     * @param url
     * @param body
     * @returns {Observable<any>}
     */
    makePostRequest(url: string, body?: any): Observable<any> {
        const headers = new HttpHeaders().set('Content-Type', 'application/json');
        return this.client.post(this.apiUrl + url, body, {headers: headers});
    }
    /**
     * Make a PUT request
     * @param url
     * @param body
     * @returns {Observable<any>}
     */
    makePutRequest(url: string, body?: any): Observable<any> {
        const headers = new HttpHeaders().set('Content-Type', 'application/json');
        return this.client.post(this.apiUrl + url, body, {headers: headers});
    }
}