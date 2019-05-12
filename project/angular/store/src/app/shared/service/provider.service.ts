import {Injectable} from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import {IAuthResponse, Item} from '../model/model';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {
  private root = `http://localhost:8000`;

  /*
  api:
    path('category', cbv_category.CategoryApi.as_view(), name='category'),
    path('category/<int:pk>', views.category_items),
    path('item', cbv_item.ItemApiView.as_view()),
    path('item/<int:pk>', cbv_item.ItemWithIdApiView.as_view()),
    path('like', views.like),
    path('comment', views.comment),
   */

  constructor(protected http: HttpClient) {
    super(http);
  }

  get_items(): Promise<Item[]> {
    return this.get(`${this.root}/api/item`, {}).then(res => res);
  }

  post_item(item: Item): Promise<Item> {
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
    return this.get(`${this.root}/api/comment/${id}`, {}).then(res => res);
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
}
