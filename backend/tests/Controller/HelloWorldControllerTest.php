<?php

namespace App\Tests\Controller;

use App\Controller\HelloWorldController;
use PHPUnit\Framework\TestCase;
use Symfony\Component\HttpFoundation\Response;

final class HelloWorldControllerTest extends TestCase
{
    /**
     * System under test.
     *
     * @var HelloWorldController
     */
    private $controller;

    protected function setUp(): void
    {
        $this->controller = new HelloWorldController();
    }

    /** @test */
    public function index_liefert_Hello_World(): void
    {
        $response = $this->controller->index();

        $this->assertEquals(Response::HTTP_OK, $response->getStatusCode());
        $this->assertContains('Hello World', $response->getContent());
    }
}
