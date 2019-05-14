import {Component, OnInit} from '@angular/core';
import {Category, emptyItem, Item} from '../../../shared/model/model';
import {ProviderService} from '../../../shared/service/provider.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.scss']
})
export class PostComponent implements OnInit {
  item: Item = emptyItem();
  categories: Category[];
  currentCategory: Category;

  constructor(
    private api: ProviderService,
    private router: Router
  ) {
  }

  ngOnInit() {
    this.api.get_categories().then(categories => {
      console.log(categories);
      this.categories = categories;
      this.currentCategory = categories[0];
    }).catch(err => {
      console.error(err);
    });
  }

  onSelectChange($event: Event) {
    console.log($event);
  }

  postIt(item: Item, currentCategory: Category) {
    console.log(item);

    const body: any = item;
    body.category_id = currentCategory.id;

    this.api.post_item(body).then(res => {
      this.router.navigate(['/']);
    }).catch(error => {
      console.error(error);
    });
  }
}