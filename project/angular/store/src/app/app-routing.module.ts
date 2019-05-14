import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {PostComponent} from './component/market/post/post.component';
import {ItemsComponent} from './component/market/items/items.component';
import {AuthenticationComponent} from './component/authentication/authentication.component';
import {DetailComponent} from './component/market/items/detail/detail.component';

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
    path: 'items',
    component: ItemsComponent
  },
  {
    path: 'items/:id',
    component: DetailComponent
  },
  {
    path: '',
    redirectTo: '/items',
    pathMatch: 'full'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
