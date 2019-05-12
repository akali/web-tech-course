import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {PostComponent} from './component/market/post/post.component';
import {AppComponent} from './app.component';
import {ItemsComponent} from './component/market/items/items.component';
import {AuthenticationComponent} from './component/authentication/authentication.component';

const routes: Routes = [
  {
    path: 'post-item',
    component: PostComponent
  },
  {
    path: 'login',
    component: AuthenticationComponent
  },
  {
    path: '',
    component: ItemsComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
