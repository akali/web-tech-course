import { Component, OnInit } from '@angular/core';
import { ITaskList } from './model/model';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'front';

  constructor(private apiService: ApiService) { }

  taskLists = Array<ITaskList>();

  taskList: ITaskList = null;

  ngOnInit(): void {
    console.log('hello!');

    this.apiService.getTaskLists().then(taskLists => {
      this.taskLists = taskLists;
    });
  }

  onTaskListClick(item) {
    this.taskList = null;
    setInterval(() => {
      this.taskList = item;
    }, 10);
  }
}
