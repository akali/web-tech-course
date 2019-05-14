import {Component, OnInit} from '@angular/core';
import {ProviderService} from '../../../shared/service/provider.service';
import {Item} from '../../../shared/model/model';
import {ActivatedRoute, Router} from '@angular/router';

@Component({
  selector: 'app-items',
  templateUrl: './items.component.html',
  styleUrls: ['./items.component.scss']
})
export class ItemsComponent implements OnInit {

  private items: Item[];

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private provider: ProviderService
  ) {
  }

  ngOnInit() {
    this.provider.get_items().then(items => {
      console.log(items);
      this.items = items;
    }).catch(error => {
      console.error(error);
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
      item.likes_count++;
    }).catch(error => {
      this.provider.delete_like(item.id).then(resp => {
        item.likes_count--;
      }).catch(error2 => {
        console.log(error);
      });
      console.log(error);
      alert('looks like you have already liked this item');
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
