import {Injectable} from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import {Category, Comment, IAuthResponse, Item} from '../model/model';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {
  private root = `http://localhost:8000`;

  constructor(protected http: HttpClient) {
    super(http);
  }

  get_items(): Promise<Item[]> {
    return this.get(`${this.root}/api/item`, {}).then(res => res);
  }

  public get_categories(): Promise<Category[]> {
    return this.get(`${this.root}/api/category`, {});
  }

  post_item(item: any): Promise<Item> {
    return this.post(`${this.root}/api/item`, item).then(res => res);
  }

  get_item(id: number): Promise<Item> {
    return this.get(`${this.root}/api/item/${id}`, {}).then(res => res);
  }

  update_item(id: number, item: Item): Promise<Item> {
    return this.put(`${this.root}/api/item/${id}`, item).then(res => res);
  }

  delete_item(id: number): Promise<Item> {
    return this.delete(`${this.root}/api/item/${id}`, {}).then(res => res);
  }

  get_comments(id: number): Promise<Comment[]> {
    return this.get(`${this.root}/api/item/${id}/comment`, {}).then(res => res);
  }

  put_comment(id: number, comment: Comment): Promise<Comment> {
    return this.post(`${this.root}/api/item/${id}/comment`, comment);
  }

  put_like(id: number): Promise<any> {
    return this.post(`${this.root}/api/like`, {
      item_id: `${id}`
    });
  }

  login(login: string, pass: string): Promise<IAuthResponse> {
    return this.post(`${this.root}/api/login/`, {
      username: login,
      password: pass
    });
  }

  logout(): Promise<any> {
    return this.post(`${this.root}/api/logout/`, {});
  }

  delete_like(id: number) {
    return this.delete(`${this.root}/api/like`, {
      item_id: id
    });
  }
}
