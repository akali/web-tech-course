import { Component, OnInit, Input } from '@angular/core';
import { ITaskList, ITask } from '../model/model';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-tasks',
  templateUrl: './tasks.component.html',
  styleUrls: ['./tasks.component.css']
})
export class TasksComponent implements OnInit {

  tasks: ITask[] = null;
  task: ITask = null;
  constructor(private apiService: ApiService) { }

  @Input() taskList: ITaskList;

  ngOnInit() {
    this.apiService.getTasksOfTaskList(this.taskList.id).then(tasks => {
      this.tasks = tasks;
      console.log(tasks);
    });
  }

  onTaskClick(stask) {
    console.log(stask);
    this.apiService.getTask(stask.id).then(task => {
      this.task = task;
    });
  }

}
