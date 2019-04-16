export interface ITask {
    id: number;
    name: string;
    due_on: Date;
    created_at: Date;
    status: string;
}

export interface ITaskList {
    id: number;
    name: string;
}
