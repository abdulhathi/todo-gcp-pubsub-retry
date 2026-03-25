import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { TodoResponse, TodoService } from '../../services/todos.service';
import { Todo } from '../../models/todo';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-todo-list',
  imports: [CommonModule, FormsModule, MatIconModule, MatButtonModule],
  templateUrl: './todo-list.html',
  styleUrl: './todo-list.scss',
})
export class TodoList implements OnInit {
  todos: Todo[] = [];
  newTodoTitle: string = '';
  showAddTodo: boolean = false;

  constructor(
    private todoService: TodoService,
    private cdr: ChangeDetectorRef,
  ) {}

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

  addTodo() {
    const todoIds = this.todos.map((t) => parseInt(t.id));
    const id = Math.max(...todoIds) + 1;
    this.todos.push({
      id: String(id),
      title: this.newTodoTitle,
      status: 'PENDING',
    });
  }

  deleteTodo(id: string) {
    console.log(id);
    this.todos = this.todos.filter((t) => t.id !== id);
    this.cdr.detectChanges();
  }

  onSave() {
    this.todoService.saveTodos(this.todos).subscribe({
      next: (data) => {
        this.todos.forEach((t) => (t.status = 'SAVED'));
        this.cdr.detectChanges();
      },
      error: (err: any) => console.log(err),
    });
  }

  onSubmit() {
    // this.todoService.submitTodos(this.todos).subscribe(() => {
    //   this.todos.forEach((t) => (t.status = 'SENT'));
    // });
  }
}
