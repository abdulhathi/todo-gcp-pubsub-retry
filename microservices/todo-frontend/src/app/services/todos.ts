import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

interface Todo {
  id: number;
  title: string;
  status: string;
}

@Injectable({
  providedIn: 'root',
})
export class Todos {
  baseUrl: string = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  getTodos() {
    return this.http.get<Todo>(`${this.baseUrl}\api\todos`);
  }
}
