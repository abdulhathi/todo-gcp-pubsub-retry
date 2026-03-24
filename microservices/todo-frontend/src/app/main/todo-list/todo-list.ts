import { Component, OnInit } from '@angular/core';
import { TodoResponse, TodoService } from '../../services/todos.service';
import { Todo } from '../../models/todo';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-todo-list',
  imports: [CommonModule, FormsModule],
  templateUrl: './todo-list.html',
  styleUrl: './todo-list.scss',
})
export class TodoList implements OnInit {
  todos: Todo[] = [];

  constructor(private todoService: TodoService) {}

  ngOnInit(): void {
    this.todoService.getTodos().subscribe({
      next: (todoResponse: TodoResponse) => {
        // console.log(todoResponse.todos);
        this.todos = todoResponse.todos;
      },
      error: (err: any) => {
        console.log(err);
      },
    });
  }

  reset(todo: any) {
    todo.title = '';
    todo.status = 'PENDING';
    todo.edited = false;
  }

  onSave() {
    // this.todoService.saveTodos(this.todos).subscribe(() => {
    //   this.todos.forEach((t) => (t.status = 'SAVED'));
    // });
  }

  onSubmit() {
    // this.todoService.submitTodos(this.todos).subscribe(() => {
    //   this.todos.forEach((t) => (t.status = 'SENT'));
    // });
  }
}
