import { BrowserModule } from '@angular/platform-browser';
import {ClassProvider, NgModule} from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AuthenticationComponent } from './component/authentication/authentication.component';
import { ItemsComponent } from './component/market/items/items.component';
import {ProviderService} from './shared/service/provider.service';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import {AuthInterceptor} from './shared/interceptor/AuthInterceptor';

@NgModule({
  declarations: [
    AppComponent,
    AuthenticationComponent,
    ItemsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [
    ProviderService,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    } as ClassProvider
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
