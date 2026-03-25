import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Todo } from '../models/todo';

export interface TodoResponse {
  status: string;
  todos: Todo[];
}

@Injectable({
  providedIn: 'root',
})
export class TodoService {
  baseUrl: string = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  getTodos() {
    return this.http.get<TodoResponse>(`${this.baseUrl}/api/todos`);
  }

  saveTodos(todos: Todo[]) {
    return this.http.post(`${this.baseUrl}/api/todos/save`, { todos: todos });
  }
}
