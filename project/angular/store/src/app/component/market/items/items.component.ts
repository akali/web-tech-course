import {Component, OnInit} from '@angular/core';
import {ProviderService} from '../../../shared/service/provider.service';
import {Category, Item} from '../../../shared/model/model';
import {ActivatedRoute, Router} from '@angular/router';

@Component({
  selector: 'app-items',
  templateUrl: './items.component.html',
  styleUrls: ['./items.component.scss']
})
export class ItemsComponent implements OnInit {

  private items: Item[];
  private filterCategory: Category;
  private categories: Category[];

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private provider: ProviderService
  ) {
  }

  ngOnInit() {
    this.provider.get_categories().then(categories => {
      this.categories = categories;
      this.filterCategory = this.categories[0];
    });
    this.filterCategory = null;
    this.provider.get_items().then(items => {
      console.log(items);
      this.items = items;
    }).catch(error => {
      console.error(error);
    });
  }

  onCategoryClick(category: Category) {
    this.filterCategory = category;
    this.provider.get_items_category(category).then(items => {
      this.items = items;
      console.log(items);
    });
  }

  onItemClick(item: Item) {
    this.router.navigate([`${item.id}`], {
      relativeTo: this.route
    });
  }

  onPostItemClick() {
    this.router.navigateByUrl('/post-item');
  }

  onLikeClick(item: Item) {
    this.provider.put_like(item.id).then(resp => {
      item.likes_count = resp.like_count;
    }).catch(error => {
      // this.provider.delete_like(item.id).then(resp => {
      //   item.likes_count--;
      // }).catch(error2 => {
      //   console.log(error);
      // });
      console.log(error);
      // alert('looks like you have already liked this item');
    });
  }

  getPictureURL(item: Item) {
    if (item.picture == null) {
      return 'https://images-na.ssl-images-amazon.com/images/I/61%2BXkFYjMFL._SL1500_.jpg';
    } else {
      console.log(item.picture);
      return this.provider.get_picture_url(item.picture);
    }
  }
}
