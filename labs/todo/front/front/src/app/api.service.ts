import { Injectable } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';
import { ITaskList, ITask } from './model/model';

@Injectable({
  providedIn: 'root'
})
export class ApiService extends MainService {

  constructor(http: HttpClient) {
    super(http);
  }

  root = 'http://localhost:8000';

  getTaskLists(): Promise<ITaskList[]> {
    return this.get(`${this.root}/api/task_lists/`, {});
  }

  getTaskList(id: number): Promise<ITaskList[]> {
    return this.get(`${this.root}/api/task_lists/${id}/`, {});
  }

  getTasksOfTaskList(id: number): Promise<ITask[]> {
    return this.get(`${this.root}/api/task_lists/${id}/tasks/`, {});
  }

  getTask(id: number): Promise<ITask> {
    return this.get(`${this.root}/api/tasks/${id}/`, {});
  }
}
